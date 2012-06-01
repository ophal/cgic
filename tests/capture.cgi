#!/usr/bin/env luajit

require [[cgic]]

cgic.init()

function cgiMain()
  cgic.writeEnvironment [[/tmp/cgic_capture.dat]]
  cgic.headerContentType [[text/html]]
  print [[<title>Captured</title>
<h1>Captured</h1>
Your form submission was captured for use in
debugging CGI code.]]
end

cgiMain()
