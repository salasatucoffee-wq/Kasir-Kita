import re, shutil, os
pkg = 'id/salasatucoffee/kasir'
dst = 'android/app/src/main/java/' + pkg
os.makedirs(dst, exist_ok=True)
for f in ('PrinterBridgePlugin.java', 'MainActivity.java'):
    shutil.copy('native/' + f, dst + '/' + f)

m = 'android/app/src/main/AndroidManifest.xml'
s = open(m).read()
perms = ['BLUETOOTH', 'BLUETOOTH_ADMIN', 'BLUETOOTH_CONNECT', 'BLUETOOTH_SCAN']
add = ''.join('    <uses-permission android:name="android.permission.%s" />\n' % p
              for p in perms if 'android.permission.%s"' % p not in s)
add += '    <uses-feature android:name="android.hardware.usb.host" android:required="false" />\n'
add += '    <uses-feature android:name="android.hardware.bluetooth" android:required="false" />\n'
s = s.replace('<application', add + '    <application', 1)
open(m, 'w').write(s)

v = 'android/variables.gradle'
t = open(v).read()
t = re.sub(r'targetSdkVersion\s*=\s*\d+', 'targetSdkVersion = 30', t)
open(v, 'w').write(t)
print('patched')
