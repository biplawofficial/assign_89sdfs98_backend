import pandas as pd
import random
from faker import Faker

# Initialize Faker for date generation
faker = Faker()

<<<<<<< HEAD

Post_Types = {
    "carousel": {"Likes": (500, 1000), "Shares": (200, 500), "Comments": (100, 300), "Views": (1000, 5000)},
    "reels": {"Likes": (1000, 5000), "Shares": (300, 1000), "Comments": (500, 1500), "Views": (5000, 20000)},
    "static_image": {"Likes": (300, 700), "Shares": (100, 300), "Comments": (50, 150), "Views": (500, 3000)},
    "video": {"Likes": (700, 2000), "Shares": (200, 700), "Comments": (300, 800), "Views": (2000, 10000)},
=======
# Define post types and engagement ranges
post_types = {
    "carousel": {"likes": (500, 1000), "shares": (200, 500), "comments": (100, 300), "views": (1000, 5000)},
    "reels": {"likes": (1000, 5000), "shares": (300, 1000), "comments": (500, 1500), "views": (5000, 20000)},
    "static_image": {"likes": (300, 700), "shares": (100, 300), "comments": (50, 150), "views": (500, 3000)},
    "video": {"likes": (700, 2000), "shares": (200, 700), "comments": (300, 800), "views": (2000, 10000)},
>>>>>>> 5508dcb018691f213d25758d87feda49a4fc50c5
}

# Time bias function
def generate_biased_time():
    # Generate times in 24-hour format
    mid_morning_times = [f"{hour:02}:{minute:02}" for hour in range(9, 12) for minute in range(0, 60, 15)]
    other_times = [f"{hour:02}:{minute:02}" for hour in range(8, 18) for minute in range(0, 60, 15) if hour < 9 or hour >= 12]
    times = mid_morning_times * 4 + other_times  # Weight mid-morning
    return random.choice(times)

<<<<<<< HEAD
# Generate 100 simulated posts
for _ in range(200):
    Post_Type = random.choice(list(Post_Types.keys()))
    metrics = Post_Types[Post_Type]
=======
# Generate posts
data = []
for i in range(1, 101):
    post_type = random.choice(list(post_types.keys()))
    metrics = post_types[post_type]
>>>>>>> 5508dcb018691f213d25758d87feda49a4fc50c5
    
    post_data = {
<<<<<<< HEAD
        "Post_ID": faker.uuid4(),
        "Post_Type": Post_Type,
        "Likes": random.randint(*metrics["Likes"]),
        "Shares": random.randint(*metrics["Shares"]),
        "Comments": random.randint(*metrics["Comments"]),
        "Views": random.randint(*metrics["Views"]),
=======
        "Post_ID": f"P{i:03}",
        "Post_Type": post_type,
        "Likes": random.randint(*metrics["likes"]),
        "Shares": random.randint(*metrics["shares"]),
        "Comments": random.randint(*metrics["comments"]),
        "Views": random.randint(*metrics["views"]),
>>>>>>> 5508dcb018691f213d25758d87feda49a4fc50c5
        "Post_Date": faker.date_between(start_date="-1y", end_date="today"),
        "Post_Time": generate_biased_time(),
    }
    data.append(post_data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Validate combined Date and Time (Optional)
df['Post_DateTime'] = pd.to_datetime(df['Post_Date'].astype(str) + ' ' + df['Post_Time'], format="%Y-%m-%d %H:%M")

# Save to CSV
df.to_csv("fsed.csv", index=False)
print(df.head())
