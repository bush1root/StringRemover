# StringRemover
String Remover from Process Hacker (Work to Minecraft)

# ⚡ How to configure?
Enter the data as written in the GUI
Tutorial: [Click](https://www.youtube.com/watch?v=47fI6JxaleM) (in Russian)

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
![Screenshot_20220824_131924](https://user-images.githubusercontent.com/100863585/186394381-77471cc0-6520-4803-b457-d1ac777beb20.png)
