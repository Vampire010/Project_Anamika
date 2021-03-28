class Addition:
    def __add__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        num3 = num1 + num2
        print(num3)

    def __mul__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        num3 = nums1 * nums2
        print(num3)


A = Addition()
A.__add__(10, 15)
A.__mul__(12, 20)
