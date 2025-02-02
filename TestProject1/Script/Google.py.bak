def Test():
 TestedApps.chrome.Run(1, True)
 chrome = Sys.Process("chrome")
 page = chrome.Page("*")
 page.ToUrl("https://www.google.com")
 textarea = page.FindElement("//form//textarea")
 textarea.Click()
 textarea.Keys("test[Enter]")
 page.wait()
 textLabel = page.FindElement("#APjFqb")
 CheckProperty(textLabel, "value", cmpEqual, "test")
 chrome.Close()
 
