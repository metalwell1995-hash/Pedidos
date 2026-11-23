import pathlib
p = pathlib.Path('android/app/src/main/AndroidManifest.xml')
t = p.read_text()
if 'RECORD_AUDIO' not in t:
    t = t.replace('<application', '<uses-permission android:name="android.permission.RECORD_AUDIO" />\n    <application', 1)
    p.write_text(t)
print(p.read_text())
