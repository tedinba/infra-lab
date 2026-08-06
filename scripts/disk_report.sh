echo "Showing the largest directories"
echo "Current date: $(date)"
echo "5 largest directories: $(du -h --max-depth=1 . | sort -hr | head -n 5)"
echo "Report completed successfully."
