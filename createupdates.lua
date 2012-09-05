#!/usr/bin/env lua
--[[

 This tool generates update archives and a matching resources.xml file
 based on the world data repository.

 It expects 'git' and 'adler32' to be available in the path.

 Configuration happens through the following environment variables:

 WORLD_DATA_REPOSITORY (example: /home/user/world/.git)
 CLIENT_UPDATES_DIR    (example: /home/user/public_html/updates)

--]]

local function checkenv(varname)
    local value = os.getenv(varname)
    if not value then
        print(varname .. ' not set')
        os.exit(1)
    end
    return value
end

local WORLD_DATA_REPOSITORY = checkenv('WORLD_DATA_REPOSITORY')
local CLIENT_UPDATES_DIR = checkenv('CLIENT_UPDATES_DIR')


local function trim(s)
    s = string.gsub(s, '^%s+', '')      -- strip preceding whitespace
    s = string.gsub(s, '%s+$', '')      -- strip trailing whitespace
    return s
end

local function capture(command)
    local f = assert(io.popen(command, 'r'))
    local s = assert(f:read('*a'))
    f:close()
    return trim(s)
end

local function execute(command)
    local result = assert(os.execute(command))
    if result ~= 0 then
        print("Error executing:")
        print(" " .. command)
        os.exit(1)
    end
end

local function git(subcommand)
    return 'git --git-dir=' .. WORLD_DATA_REPOSITORY .. ' ' .. subcommand
end

local function adler32(file)
    return string.sub(capture('adler32 ' .. file), -8)
end

local function last_revision(paths)
    local output = capture(git('log -1 --oneline -- ' .. paths))
    return assert(string.match(output, '(%w+) '))
end

local function exists(filename)
    local file = io.open(filename, "r")
    if file then
        io.close(file)
        return true
    end
    return false
end


local packages = {
    {
        name = "definitions",
        paths = {
            "attributes.xml",
            "effects.xml",
            "emotes.xml",
            "equip.xml",
            "hair.xml",
            "items.xml",
            "maps.xml",
            "monsters.xml",
            "npcs.xml",
            "paths.xml",
            "permissions.xml",
            "skills.xml",
            "specials.xml",
            "status-effects.xml",
            "units.xml",
        },
    },
    { name = "music", type = "music", required = "no", paths = { "music" }, },
    { name = "sound", paths = { "sfx" }, },
    { name = "maps", paths = { "maps" }, },
    {
        name = "graphics",
        paths = {
            "automapping",
            "icons",
            "items",
            "minimaps",
            "particles",
            "sprites",
            "tiles",
        },
    },
}

local resources_lines = {
    '<?xml version="1.0"?>',
    '<updates>',
}

for i=1,#packages do
    local package = packages[i]
    local paths = table.concat(package.paths, ' ')
    local revision = last_revision(paths)
    local filename = package.name .. "-" .. revision .. ".zip"
    local fullname = CLIENT_UPDATES_DIR .. '/' .. filename

    if exists(fullname) then
        print("Skipping " .. filename .. " (already exists)")
    else
        print("Creating " .. filename)
        execute(git('archive HEAD --output=' .. fullname .. ' ' .. paths))
    end

    local type = package.type or "data"
    local hash = adler32(fullname)
    local line = ' <update type="' .. type .. '"'
    if package.required == "no" then
        line = line .. ' required="no"'
    end
    line = line .. ' file="' .. filename .. '"'
    line = line .. ' hash="' .. hash .. '" '
    if package.description then
        line = line .. ' description="' .. package.description .. '"'
    end
    line = line .. '/>'
    table.insert(resources_lines, line)
end

table.insert(resources_lines, '</updates>')

print("Writing resources.xml")
local file = io.open(CLIENT_UPDATES_DIR .. "/resources.xml", "w")
file:write(table.concat(resources_lines, '\n') .. '\n')
file:close()
