import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        time TEXT NOT NULL,
        description TEXT NOT NULL,
        url TEXT NOT NULL
    )
''')
conn.commit()

def add_video():
    title = input("Enter the title of the video: ")
    time = input("Enter the time of the video: ")
    description = input("Enter the description: ")
    url = input("Enter the URL: ")
    cursor.execute(
        "INSERT INTO videos (title, time, description, url) VALUES (?, ?, ?, ?)",
        (title, time, description, url)
    )
    conn.commit()
    print("Video added successfully.")

def update_video(video_id):
    cursor.execute("SELECT * FROM videos WHERE id=?", (video_id,))
    video = cursor.fetchone()
    if not video:
        print("Video not found.")
        return
    print(f"Current title: {video[1]}")
    new_title = input("Enter new title (leave blank to keep current): ") or video[1]
    print(f"Current time: {video[2]}")
    new_time = input("Enter new time (leave blank to keep current): ") or video[2]
    print(f"Current description: {video[3]}")
    new_description = input("Enter new description (leave blank to keep current): ") or video[3]
    print(f"Current URL: {video[4]}")
    new_url = input("Enter new URL (leave blank to keep current): ") or video[4]
    cursor.execute(
        "UPDATE videos SET title=?, time=?, description=?, url=? WHERE id=?",
        (new_title, new_time, new_description, new_url, video_id)
    )
    conn.commit()
    print("Video updated successfully.")

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    for row in videos:
        print(f"ID: {row[0]}, Title: {row[1]}, Time: {row[2]}, Description: {row[3]}, URL: {row[4]}")

def delete_video(video_id):
    cursor.execute("SELECT * FROM videos WHERE id=?", (video_id,))
    if not cursor.fetchone():
        print("Video not found.")
        return
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()
    print("Video deleted successfully.")

def main():
    while True:
        print("\nYOUTUBE MANAGER\n")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            video_id = input("Enter the ID of the video to update: ")
            if video_id.isdigit():
                update_video(int(video_id))
            else:
                print("Invalid ID.")
        elif choice == '4':
            video_id = input("Enter the ID of the video to delete: ")
            if video_id.isdigit():
                delete_video(int(video_id))
            else:
                print("Invalid ID.")
        elif choice == '5':
            print("Exiting the YouTube Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()