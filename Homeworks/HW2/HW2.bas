Attribute VB_Name = "Module1"
Sub easy()
    Dim i As Long
    Dim j As Long
    Dim ticknum As Integer
    ticknum = 1
    Dim ticker() As String
    Dim tic As Variant
    
    'count the last row
    lastrow = Cells(Rows.Count, 1).End(xlUp).row
    'count number of tickers
    For i = 2 To lastrow
        If Cells(i, 1) <> Cells(i + 1, 1) Then
            ticknum = ticknum + 1
        End If
    Next i
    
    'print ticker
    For j = 1 To ticknum
        ReDim ticker(1 To ticknum)
        For i = 2 To lastrow
            If Cells(i, 1) <> Cells(i + 1, 1) Then
                ticker(j) = Cells(i, 1)
            End If
        Next i
    Next j
    Cells(j + 1, 10) = ticker(j)
End Sub
    
    
