
#Your Wifi connection data
local SSID = "5GH"
local SSID_PASSWORD = "112330720040719440"
local LED_PIN = 3 -- GPIO0

local function connect (conn, data)
    local data

    conn:on ("receive",
        function (cn, req_data)
            data = get_http_req (req_data)

            -- print data
            for k, v in pairs( data ) do
                if k ~= "GET" then
                    print(k, "=",v)
                else
                    print(k, ":")
                    for j, w in pairs( v ) do
                        print("  ", j, " = ", w)
                    end
                end
            end

            -- check if LED parameter contained
            if data["GET"]["led"] ~= nil then
                if data["GET"]["led"] == "on" or data["GET"]["led"] == "1" then

                    -- turn LED on
                    gpio.write(LED_PIN, gpio.HIGH)
                    cn:send ("LED was turned ON")

                elseif data["GET"]["led"] == "off" or data["GET"]["led"] == "0" then

                    -- turn LED off
                    gpio.write(LED_PIN, gpio.LOW)
                    cn:send ("LED was turned OFF")

                else
                    cn:send ("Invalid Input")
                end
            else
                cn:send ("Invalid Input")
            end


            -- Close the connection for the request
            cn:on("sent",function(cn) cn:close() end)
        end)
end

function wait_for_wifi_conn ( )
   tmr.alarm (1, 1000, 1, function ( )
      if wifi.sta.getip ( ) == nil then
         print ("Waiting for Wifi connection")
      else
         tmr.stop (1)
         print ("ESP8266 mode is: " .. wifi.getmode ( ))
         print ("The module MAC address is: " .. wifi.ap.getmac ( ))
         print ("Config done, IP is " .. wifi.sta.getip ( ))
      end
   end)
end


function get_http_req(request)

    local t = {}
    local buf = "";
    local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
    if(method == nil)then
        _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");
    end
    local _GET = {}
    if (vars ~= nil)then
        for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do
            _GET[k] = v
        end
    end

    t["METHOD"] = method
    t["PATH"] = path
    t["GET"] = _GET
    return t
end


-- setup GPIO
gpio.mode(LED_PIN, gpio.OUTPUT)

-- Configure the ESP as a station (client)
wifi.setmode (wifi.STATION)
wifi.sta.config (SSID, SSID_PASSWORD)
wifi.sta.autoconnect (1)

-- Hang out until we get a wifi connection before the httpd server is started.
wait_for_wifi_conn ( )

-- Create the httpd server
svr = net.createServer (net.TCP, 30)

-- Server listening on port 80, call connect function if a request is received
svr:listen (80, connect)