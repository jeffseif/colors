# colors

Helpers for printing colored text in bash

## Install to the system

```bash
pip install git+https://github.com/jeffseif/colors.git@main
```

## Use in a package

```diff
diff --git a/requirements.txt b/requirements.txt
index 762212b..545d0cf 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,3 +1,4 @@
+-e git://github.com/jeffseif/colors.git#egg=colors
diff --git a/setup.py b/setup.py
index 6b12258..cb27369 100644
--- a/setup.py
+++ b/setup.py
@@ -10,6 +10,9 @@ from switch import __version__
 setup(
+    dependency_links=[
+        'https://github.com/jeffseif/colors.git#egg=colors',
+    ],
```

```python
>>> from colors import RED
>>> print(RED('jeff'))
jeff
```
