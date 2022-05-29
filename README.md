# hm8_Nav2 for FRA502
### Step1: spawn prototype robot.
```
ros2 launch hm8_description spawn.launch.py 
```
### Step2: run Nav2 package.
```
ros2 launch hm8_navigation2 nav2.launch.py
```

### Step3: Go to directory ```/my_package/my_package``` to open ```goal.py```file.

#### เมื่อ run ไฟล์ goal.py จะเป็นการ initial pose, set goal pose และ บอกว่าทำงานเสร็จแล้วหรือยัง

- โดย initial pose สามารถกำหนดได้ผ่าน parameter เหล่านี้

![](image/initial.png)

- กำหนด goal pose ได้ผ่าน parameter เหล่านี้

![](image/Goal.png)

- เมื่อ Navigation ทำงานเสร็จจะส่งผลลัพธ์ออกมา

![](image/result.png)



####################################################

ตอนนี้ทำให้ spawn หุ่นที่จะใช้จริงใน sim ได้แล้ว เพื่อที่จะทดลองใช้ร่วมกับ Navigation

```

ros2 launch housem8 spawn_gazebo.launch.py

```
