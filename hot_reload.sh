
#!/bin/bash
echo "Watching for changes..."
find . -name "*.py" | entr -r python3 main.py
