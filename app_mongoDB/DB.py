from pymongo import MongoClient

client = MongoClient("mongodb+srv://sarvesh_bxbx:Bxbx081205@cluster0.uvpawjz.mongodb.net/")
db = client["Youtube"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    video_collection.find({})
    for video in video_collection.find({}):
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    
    video_collection.update_one({"_id": video_id}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})

def main():
    while True:
        print("\nMenu:")
        print("1. List All Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id,name,time)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
