data segment
    string db "Enter a Charater : $"
data ends

code segment
    start:mov ax, data
    mov ds, ax
    
    lea dx, string
    mov ah, 09h
    int 21h
    
    mov ah, 01h
    int 21h
    
    mov dl, al
    mov ah, 02h
    int 21h
code ends
end start