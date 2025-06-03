VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmDescriptive 
   Caption         =   "Panel Data Analysis"
   ClientHeight    =   8205.001
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   8145
   OleObjectBlob   =   "frmDescriptive.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "frmDescriptive"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub btnClean_Click()

frmDescriptive.cmbY = ""
frmDescriptive.cmbX1 = ""
frmDescriptive.cmbX2 = ""
frmDescriptive.cmbX3 = ""
frmDescriptive.cmbX4 = ""
frmDescriptive.cmbX5 = ""
frmDescriptive.cmbX6 = ""
frmDescriptive.cmbX7 = ""
frmDescriptive.cmbX8 = ""

End Sub

Private Sub btnExit_Click()
Unload Me
End Sub

Private Sub btnPrint_Click()
Call RunPythonScript("run_print")
End Sub

Private Sub btnRead_Click()
    Call RunPythonScript("run_read")
    Call FillComboBoxesFromColumns
End Sub

Private Sub btnAnalysis_Click()
    Dim selectedColumns As Collection
    Set selectedColumns = New Collection

    ' Read comboboxes
    On Error Resume Next
    If Trim(Me.cmbY.Value) <> "" Then selectedColumns.Add Me.cmbY.Value
    If Trim(Me.cmbX1.Value) <> "" Then selectedColumns.Add Me.cmbX1.Value
    If Trim(Me.cmbX2.Value) <> "" Then selectedColumns.Add Me.cmbX2.Value
    If Trim(Me.cmbX3.Value) <> "" Then selectedColumns.Add Me.cmbX3.Value
    If Trim(Me.cmbX4.Value) <> "" Then selectedColumns.Add Me.cmbX4.Value
    If Trim(Me.cmbX5.Value) <> "" Then selectedColumns.Add Me.cmbX5.Value
    If Trim(Me.cmbX6.Value) <> "" Then selectedColumns.Add Me.cmbX6.Value
    If Trim(Me.cmbX7.Value) <> "" Then selectedColumns.Add Me.cmbX7.Value
    If Trim(Me.cmbX8.Value) <> "" Then selectedColumns.Add Me.cmbX8.Value
    On Error GoTo 0

    ' Cancel if there are not selected headers
    If selectedColumns.Count = 0 Then
        MsgBox "Please select at least one variable (Y or X1�X8) before running the analysis.", vbExclamation
        Exit Sub
    End If

    ' Manually convert to JSON
    Dim json As String
    Dim i As Long
    json = "["
    For i = 1 To selectedColumns.Count
        json = json & """" & selectedColumns(i) & """"
        If i < selectedColumns.Count Then json = json & ","
    Next i
    json = json & "]"

    ' Save JSON file
    Dim fso As Object, ts As Object
    Dim jsonPath As String
    jsonPath = "C:\Python\ProjectStats\data\selected_columns.json"

    Set fso = CreateObject("Scripting.FileSystemObject")
    Set ts = fso.CreateTextFile(jsonPath, True)
    ts.Write json
    ts.Close

    ' Run Python descriptive command
    Call RunPythonScript("run_descriptive")
End Sub

Private Sub btnResults_Click()
    Call RunPythonScript("run_display")
End Sub

Private Sub RunPythonScript(command As String)
    Dim pythonExePath As String
    Dim scriptPath As String
    Dim shell As Object
    Dim fullCommand As String

    ' Path to the Python executable file inside .venv
    pythonExePath = "C:\Python\ProjectStats\.venv\Scripts\python.exe"
    
    ' Path to the main file 
    scriptPath = "C:\Python\ProjectStats\src\main.py"
    
    ' Develop command with argument
    fullCommand = """" & pythonExePath & """ """ & scriptPath & """ " & command

    ' Execute the command using Powershell or cmd (silent mode or window)
    Set shell = CreateObject("WScript.Shell")
    shell.Run fullCommand, 1, True  ' 1 = normal window, False = do not wait until it's done
End Sub
Sub FillComboBoxesFromColumns()
    Dim fso As Object, ts As Object
    Dim jsonText As String, colArray() As String
    Dim i As Long
    Dim columnsPath As String
    
    columnsPath = "C:\Python\ProjectStats\data\columns.json"

    ' Check if the file exists
    Set fso = CreateObject("Scripting.FileSystemObject")
    If Not fso.FileExists(columnsPath) Then
        MsgBox "File columns.json not found. Please run 'Read Data' first.", vbExclamation
        Exit Sub
    End If

    ' Read the JSON file content
    Set ts = fso.OpenTextFile(columnsPath, 1)
    jsonText = ts.ReadAll
    ts.Close

    ' Basic parsing: remove brackets and quotes
    jsonText = Replace(jsonText, "[", "")
    jsonText = Replace(jsonText, "]", "")
    jsonText = Replace(jsonText, """", "")
    colArray = Split(jsonText, ",")

    ' Clear all ComboBoxes
    'Me.cmbEntity.Clear
    'Me.cmbTime.Clear
    Me.cmbY.Clear

    Dim j As Long
    For j = 1 To 8
        Me.Controls("cmbX" & j).Clear
    Next j

    ' Fill all ComboBoxes with the same column names
    For i = 0 To UBound(colArray)
        Dim colName As String
        colName = Trim(colArray(i))
        If colName <> "" Then
            'Me.cmbEntity.AddItem colName
            'Me.cmbTime.AddItem colName
            Me.cmbY.AddItem colName
            For j = 1 To 8
                Me.Controls("cmbX" & j).AddItem colName
            Next j
        End If
    Next i
End Sub
