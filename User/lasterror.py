import sublime
import sublime_plugin
import urllib
import httplib
import sys
import re

print "last error loaded"
class LastError(sublime_plugin.TextCommand):

	def run(self, edit):
		try:
			msg = "lasterror"
			host = "127.0.0.1:8080"
			http = httplib.HTTPConnection(host)
			http.putrequest("POST", "/lasterror/")
			http.putheader("content-length", str(len(msg)))
			http.endheaders()

			http.send(msg)
			response = http.getresponse()
			data = response.read()
			print data
			# self.view.window().run_command("show_panel", {"panel": "console"})
		except:
			print self.view.file_name(), "Last error failed. %s" % sys.exc_info()[0]

		lineNumber = (int) (re.search(r':(.+?):', data).group(0)[1:-1])
		# print lineNumber
		script_with_error = re.search(r'\"(.+?)\"', data).group(0)[1:-1].replace('/', '\\')

		script_path = "%s%s%s" % (
		                                sublime.active_window().folders()[0],
		                                "\src\\",
		                                script_with_error
		                            )
		script_path = script_path.replace("C:\\", "/C/").replace('\\', '/')
		sublime.active_window().run_command('open_file', {"file": script_path})
		sublime.active_window().run_command("goto_line", {"line": lineNumber} )
		sublime.active_window().run_command("move_to", {"to": "hardeol", "extend": True})
		# if sublime.active_window().active_view():
