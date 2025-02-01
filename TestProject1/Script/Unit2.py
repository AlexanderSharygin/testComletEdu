
def Test1():
  if not Aliases.notepad_.Exists:
    TestedApps.notepad.Run(1, True)
  notepad_ = Aliases.notepad_
  notepad_.wndNotepad.MainMenu.Click("Файл|Закрыть все")
  if notepad_.dlg_.Exists:
      if notepad_.dlg_.btn_2.Exists:
        notepad_.dlg_.btn_2.ClickButton() 
      else:
        notepad_.dlg_.btn_.ClickButton()
  notepad_.wndNotepad.Scintilla.Keys("test")
  notepad_.wndNotepad.Scintilla.Keys("[Enter]")
  notepad_.wndNotepad.Scintilla.Keys("newTest")  
  notepad_.wndNotepad.Close()