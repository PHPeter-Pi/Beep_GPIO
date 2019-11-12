#!/bin/sh

# シンボリック・リンク経由での利用のための絶対パス
PATH_FILE_SCRIPT=$(readlink $0)
PATH_DIR_CURR=$(cd $(dirname ${PATH_FILE_SCRIPT:-$0}); pwd)

if [ $# -ne 1 ]; then
  exit 0
fi

case "${1}" in
  ng ) python $PATH_DIR_CURR/beep_ng.py ;;
  ok ) python $PATH_DIR_CURR/beep_ok.py ;;
  ready ) python $PATH_DIR_CURR/beep_ready.py ;;
esac
