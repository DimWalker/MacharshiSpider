import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO
    format='%(asctime)s - %(message)s',  # 日志格式
    filename='file_monitor.log',  # 日志文件名
    filemode='a'  # 追加模式
)

# 自定义事件处理类
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 当文件或目录被修改时触发
        logging.info(f'File {event.src_path} has been modified')

    def on_created(self, event):
        # 当文件或目录被创建时触发
        logging.info(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        # 当文件或目录被删除时触发
        logging.info(f'File {event.src_path} has been deleted')

    def on_moved(self, event):
        # 当文件或目录被移动时触发
        logging.info(f'File {event.src_path} has been moved to {event.dest_path}')

if __name__ == "__main__":
    # 要监控的目录路径
    path = r"D:\Games\Mecharashi"

    # 创建事件处理器
    event_handler = MyHandler()

    # 创建观察者
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # 启动观察者
    observer.start()
    logging.info(f"Monitoring directory '{path}' for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 当用户按下 Ctrl+C 时停止观察者
        observer.stop()
        logging.info("File monitoring stopped.")

    # 等待观察者线程结束
    observer.join()