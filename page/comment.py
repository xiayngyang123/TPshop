import time

from common.base import Base


class Comment(Base):
    """封装表现层"""
    my_loc = ("xpath", "//*[@text='我的']")  # 我的余额(个人中心)
    wait_comment_loc= ("xpath", "//*[@text='待评价']")  # 待评价
    comment_loc = ("xpath", "//*[@text='评价晒单']")  # 评价晒单按钮（一组元素）
    input_comment_loc = ("xpath", "//*[@text='请输入评价']")  # 输入评价内容
    add_photo_loc = ("id", "com.tpshop.malls:id/add_img")  # 上传照片
    select_photo_loc = ("xpath", "//*[@text='从相册选择']")  # 从相册选择
    comment_grade1_loc = ("id", "com.tpshop.malls:id/star1_btn")  # 评价等级1颗星
    comment_grade2_loc = ("id", "com.tpshop.malls:id/star2_btn")  # 评价等级2颗星
    comment_grade3 = ("id", "com.tpshop.malls:id/star3_btn")  # 评价等级3颗星
    comment_grade4 = ("id", "com.tpshop.malls:id/star4_btn")  # 评价等级4颗星
    comment_grade5 = ("id", "com.tpshop.malls:id/star5_btn")  # 评价等级5颗星
    submit_loc = ("xpath", "//*[@text='提交']")   # 提交按钮
    succeed_loc = ("xpath", "//*[@text='评论成功']")  # 评论成功
    stop_comment_coordinate=[425,122]   #已评价坐标x=425,y=122
    look_button_loc=("id","com.tpshop.malls:id/order_show_btn")#查看评价(一组元素)
    look_comment_loc=("id","com.tpshop.malls:id/comment_content_tv")#查看评价内容

    """封装操作层"""
    def my (self):
        """进入个人中心"""
        self.click(self.my_loc)
    def wai_comment(self):
        """点击待评价"""
        self.click(self.wait_comment_loc)
    def comment_goods(self):
        """点击第一个商品评价"""
        elements=self.find_elements(self.comment_loc)
        self.element_click(elements[0])

    def input_comment(self,text):
        """输入评价内容"""
        self.send_keys(self.input_comment_loc,text=text)
    def comment_grade(self):
        """点击评价等级五颗星"""
        self.click_group(self.comment_grade5)

    def submit(self):
        """点击提交"""
        self.click(self.submit_loc)

    def stop_comment(self):
       """点击已评价"""
       self.tap(x=self.stop_comment_coordinate[0],y=self.stop_comment_coordinate[1])

    def  look_button(self):
        """点击查看评价按钮"""
        elements=self.find_elements(self.look_button_loc)
        self.element_click(elements[0])

    def look_comment(self):
        """获取已评价内容"""
        elements=self.find_elements(self.look_comment_loc)
        content=elements[0].get_attribute("text")
        return content

if __name__ == '__main__':
    driver = open_mobile()
    com = Comment(driver)
    time.sleep(2)
    # 我的
    com.my()
    # 点击待评价
    com.wai_comment()
    # # 点击第一个商品
    # com.comment_goods()
    # # 输入评价内容
    # text = "很好,非常好"
    # com.input_comment(text=text)
    # # 点击星星
    # com.comment_grade1()
    # # 提交
    # com.submit()
    time.sleep(3)
    # 点击已评价
    com.stop_comment()
    # 点击查看评价按钮
    com.look_button()
    # 获取评价内容
    connect = com.look_comment()
    print(connect)




