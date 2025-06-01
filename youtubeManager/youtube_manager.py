import json

def load_data():
    try:
        with open('videos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No data file found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Data file is empty or corrupted. Starting with an empty list.")
        return []

def save_data_helper(videos):
    with open('videos.json', 'w') as file:
        json.dump(videos, file, indent=4)
    print("Data saved successfully.")

def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['title']}, Description: {video['description']}, URL: {video['url']}")

def add_video(videos):
    input_title = input("Enter the video title: ")
    input_description = input("Enter the video description: ")
    input_url = input("Enter the video URL: ")
    videos.append({"title": input_title, "description": input_description, "url": input_url})
    save_data_helper(videos)
    print("Video added successfully.")

def update_video(videos):
    if not videos:
        print("No videos to update.")
        return
    list_all_videos(videos)
    try:
        idx = int(input("Enter the number of the video to update: ")) - 1
        if idx < 0 or idx >= len(videos):
            print("Invalid selection.")
            return
        print("Leave blank to keep current value.")
        title = input(f"New title (current: {videos[idx]['title']}): ") or videos[idx]['title']
        description = input(f"New description (current: {videos[idx]['description']}): ") or videos[idx]['description']
        url = input(f"New URL (current: {videos[idx]['url']}): ") or videos[idx]['url']
        videos[idx] = {"title": title, "description": description, "url": url}
        save_data_helper(videos)
        print("Video updated successfully.")
    except ValueError:
        print("Invalid input.")

def delete_video(videos):
    if not videos:
        print("No videos to delete.")
        return
    list_all_videos(videos)
    try:
        idx = int(input("Enter the number of the video to delete: ")) - 1
        if idx < 0 or idx >= len(videos):
            print("Invalid selection.")
            return
        deleted = videos.pop(idx)
        save_data_helper(videos)
        print(f"Deleted video: {deleted['title']}")
    except ValueError:
        print("Invalid input.")

def main():
    print("Welcome to the YouTube Manager!")
    print("This program allows you to manage your YouTube videos.")
    print("You can list, add, update, and delete videos.")
    print("Let's get started!\n")

    videos = load_data()

    while True:
        print("\n YOUTUBE MANAGER \n")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos(videos)
        elif choice == "2":
            add_video(videos)
        elif choice == "3":
            update_video(videos)
        elif choice == "4":
            delete_video(videos)
        elif choice == "5":
            print("Exiting the YouTube Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
