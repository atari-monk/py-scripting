You can use **PowerShell (ps1)** or **Command Prompt (cmd)** commands to list the contents of a subfolder while remaining in your current directory (`C:\atari-monk\code\py-scripting`).  

---

### **1. Using Command Prompt (`cmd`)**
#### **List Contents of a Subfolder**
```cmd
dir "subfolder_name"
```
Example:
```cmd
dir "scripts"
```

#### **List Only Files (Exclude Folders)**
```cmd
dir "scripts\*" /A-D
```

#### **List Only Subdirectories**
```cmd
dir "scripts\" /AD
```

---

### **2. Using PowerShell (`ps1`)**
#### **List Contents of a Subfolder**
```powershell
Get-ChildItem -Path .\subfolder_name
```
Example:
```powershell
Get-ChildItem -Path .\scripts
```

#### **List Only Files (Exclude Folders)**
```powershell
Get-ChildItem -Path .\scripts -File
```

#### **List Only Subdirectories**
```powershell
Get-ChildItem -Path .\scripts -Directory
```

#### **Print Just Names (Clean Output)**
```powershell
(Get-ChildItem -Path .\scripts).Name
```

---

### **3. One-Liner for Quick Use**
If you're in `C:\atari-monk\code\py-scripting` and want to check `scripts`:
```cmd
:: CMD
dir scripts
```
```powershell
# PowerShell
ls scripts  # (ls is an alias for Get-ChildItem)
```

---

### **Summary**
- **CMD:** `dir "subfolder"`  
- **PowerShell:** `Get-ChildItem -Path .\subfolder` (or `ls subfolder`)  

Both methods **keep you in the current directory** while inspecting the subfolder's contents. 🚀