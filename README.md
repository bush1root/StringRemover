# StringRemover
String Remover from Process Hacker (Work to Minecraft)

# ⚡ How to configure?
Install Modules: pip install pymem / pip install pyqt5
Enter the data as written in the GUI  
Tutorial: [Click](https://www.youtube.com/watch?v=aGYK2wzY4so) (in Russian)

# ❓ How it Works?
```python
    def remove(self):
        try:
           pymem.memory.write_string(pymem.process.open(int(self.lineEdit.text(), 0)), int(self.lineEdit_2.text(), 0), bytes(int(self.lineEdit_3.text(), 0)))
           print("Done!")
        except:
           print("Error :(")
``` 

# 📱 Screenshots
![Screenshot_20220824_132549](https://user-images.githubusercontent.com/100863585/186395757-820ed4ab-5115-4db6-9970-76d1369b8505.png)
