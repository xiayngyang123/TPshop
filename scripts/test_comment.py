import time

import allure
import pytest

from page.comment import Comment

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestComment:
    @allure.step(title='商品评价')
    def test_comment(self,open_mobile):
        """测试商品评价"""
        com = Comment(open_mobile)
        # 我的
        allure.attach('个人中心', '进入个人中心')
        com.my()
        # 点击待评价
        allure.attach('待评价', '点击待评价')
        com.wai_comment()
        # 点击第一个商品
        allure.attach('评价商品', '进入商品评价页面')
        com.comment_goods()
        # 输入评价内容
        text="很好,非常好"
        com.input_comment(text=text)
        allure.attach('输入评价内容', f'评价内容:{text}')
        # 点击评价等级(星星)
        allure.attach('评价等级', '一星好评')
        com.comment_grade()
        # 提交
        allure.attach('提交', '提交评级')
        com.submit()
        time.sleep(3)
        #点击已评价
        allure.attach('已评价', '进入已评价')
        com.stop_comment()
        #点击查看评价按钮
        allure.attach('查看评价', '点击查看评价')
        com.look_button()
        #获取评价内容
        connect=com.look_comment()
        allure.attach('获取评价内容', f'评价后的内容:{connect}')
        #关闭手机
        open_mobile.quit()
        #断言已评价的内容是不是,我输入的评价内容
        if connect==text:
            assert 1
            allure.attach('断言', f'评价的内容:{text},查看刚才评价的内容{connect}')
        else:
            print("有BUG了")


if __name__ == '__main__':
    pytest.main("-r test_buy_goods.py")