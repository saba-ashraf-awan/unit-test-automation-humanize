#!/usr/bin/env bash
# Usage: ./run_tests.sh [all|smoke|regression|boundary|ecp|datadriven|negative|saba|maryum|parallel]
cd "$(dirname "$0")"
case "${1:-all}" in
  parallel) pytest -n auto --dist loadfile --html=report.html --self-contained-html ;;
  all)      pytest -v --html=report.html --self-contained-html ;;
  *)        pytest -m "$1" ;;
esac
