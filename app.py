from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({
        "uptime": time.time() - psutil.boot_time(),           # זמן מהרגע שהמחשב עלה
        "cpu_percent": psutil.cpu_percent(interval=1),        # שימוש CPU
        "memory": psutil.virtual_memory()._asdict()           # מצב הזיכרון
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
