class YouTubeVideo:
    def __init__(self, title, views, likes=0):
        self.title = title              # ویژگی عمومی
        self.__views = views            # ویژگی خصوصی (با دو زیرخط)
        self.__likes = likes            # ویژگی خصوصی برای بونوس

    # ---------- Getter و Setter برای Views ----------
    @property
    def views(self):
        """Getter: مقدار views را برمی‌گرداند"""
        return self.__views

    @views.setter
    def views(self, value):
        """Setter: فقط مقدار غیرمنفی را قبول می‌کند"""
        if value < 0:
            print("Views cannot be negative!")
        else:
            self.__views = value

    # ---------- Getter و Setter برای Likes (بونوس) ----------
    @property
    def likes(self):
        """Getter: مقدار likes را برمی‌گرداند"""
        return self.__likes

    @likes.setter
    def likes(self, value):
        """Setter: فقط مقدار غیرمنفی را قبول می‌کند"""
        if value < 0:
            print("Likes cannot be negative!")
        else:
            self.__likes = value

    # ---------- متد نمایش اطلاعات ----------
    def display_info(self):
        """نمایش عنوان و تعداد بازدیدها (و لایک‌ها برای بونوس)"""
        print(f"Title: {self.title}")
        print(f"Views: {self.views}")
        print(f"Likes: {self.likes}")   # برای بونوس


# ---------- ایجاد شیء ----------
video = YouTubeVideo("Python Tutorial", 1500, 100)  # با ۱۰۰ لایک اولیه

# ---------- اجرای تسک‌های خواسته شده ----------
print("--- 1. Display video information ---")
video.display_info()

print("\n--- 2. Update views to 2500 ---")
video.views = 2500

print("\n--- 3. Display updated views ---")
print(f"Updated views: {video.views}")

print("\n--- 4. Try setting views to -100 ---")
video.views = -100   # این مقدار رد می‌شود و پیام خطا چاپ می‌شود

print("\n--- 5. Display final video information ---")
video.display_info()

# ---------- تست بخش بونوس (Likes) ----------
print("\n--- Bonus: Testing Likes ---")
video.likes = 200
print(f"Likes after update: {video.likes}")
video.likes = -50   # این مقدار رد می‌شود
print(f"Likes after invalid update: {video.likes}")