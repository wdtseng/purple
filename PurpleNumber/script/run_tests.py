#!/usr/bin/python
import glob
import os
import sys
import argparse
import unittest


def run_tests(src_dir, test_dir):
    sys.path.insert(0, src_dir)
    suite = unittest.defaultTestLoader.discover(test_dir, "*_test.py")
    unittest.TextTestRunner(verbosity=2).run(suite)

def include_app_engine_path(DIR_PATH):
    EXTRA_PATHS = [
      DIR_PATH,
      os.path.join(DIR_PATH, 'lib', 'antlr3'),
      os.path.join(DIR_PATH, 'lib', 'django-0.96'),
      os.path.join(DIR_PATH, 'lib', 'fancy_urllib'),
      os.path.join(DIR_PATH, 'lib', 'ipaddr'),
      os.path.join(DIR_PATH, 'lib', 'jinja2-2.6'),
      os.path.join(DIR_PATH, 'lib', 'protorpc'),
      os.path.join(DIR_PATH, 'lib', 'PyAMF'),
      os.path.join(DIR_PATH, 'lib', 'markupsafe'),
      os.path.join(DIR_PATH, 'lib', 'webob_0_9'),
      os.path.join(DIR_PATH, 'lib', 'webapp2-2.5.2'),
      os.path.join(DIR_PATH, 'lib', 'yaml', 'lib'),
      os.path.join(DIR_PATH, 'lib', 'simplejson'),
      os.path.join(DIR_PATH, 'lib', 'google.appengine._internal.graphy'),
    ]
    sys.path = EXTRA_PATHS + sys.path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all unit tests in test.")
    parser.add_argument("app_engine_path",
                        help=("path to the app engine directory. "
                              "Default: /usr/local/google_appengine"),
                        nargs="?",
                        default="/usr/local/google_appengine")
    args = parser.parse_args()

    include_app_engine_path(args.app_engine_path)
    run_tests("src", "test")
