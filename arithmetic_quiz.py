import random
import operator

class ArithmeticQuiz:
    """自动算数题生成和验证程序"""
    
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        self.correct_count = 0
        self.total_count = 0
    
    def generate_question(self):
        """生成随机算术题"""
        # 随机选择两个数字 (1-100)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        # 随机选择运算符
        op = random.choice(list(self.operations.keys()))
        
        # 避免除以零
        if op == '/' and num2 == 0:
            num2 = random.randint(1, 100)
        
        return num1, num2, op
    
    def calculate(self, num1, num2, op):
        """计算答案"""
        try:
            result = self.operations[op](num1, num2)
            # 除法结果保留两位小数
            if op == '/':
                result = round(result, 2)
            return result
        except Exception as e:
            print(f"计算错误: {e}")
            return None
    
    def ask_question(self):
        """提出一个问题并获取用户答案"""
        num1, num2, op = self.generate_question()
        correct_answer = self.calculate(num1, num2, op)
        
        print(f"\n题目: {num1} {op} {num2} = ?")
        
        try:
            user_answer = float(input("你的答案: "))
            self.total_count += 1
            
            # 检查答案（处理浮点数精度问题）
            if abs(user_answer - correct_answer) < 0.01:
                print(f"✓ 正确！答案是 {correct_answer}")
                self.correct_count += 1
                return True
            else:
                print(f"✗ 错误！正确答案是 {correct_answer}")
                return False
        except ValueError:
            print("请输入有效的数字！")
            self.total_count += 1
            return False
    
    def show_stats(self):
        """显示统计信息"""
        if self.total_count == 0:
            print("\n还没有做任何题目。")
            return
        
        accuracy = (self.correct_count / self.total_count) * 100
        print(f"\n========== 统计信息 ==========")
        print(f"总题数: {self.total_count}")
        print(f"正确数: {self.correct_count}")
        print(f"错误数: {self.total_count - self.correct_count}")
        print(f"正确率: {accuracy:.1f}%")
        print(f"=============================\n")
    
    def run(self):
        """运行程序"""
        print("欢迎使用自动算数题生成器！")
        print("输入 'q' 退出程序\n")
        
        while True:
            try:
                user_input = input("按 Enter 开始下一题 (或输入 'q' 退出, 's' 显示统计): ").strip().lower()
                
                if user_input == 'q':
                    print("\n感谢使用！")
                    self.show_stats()
                    break
                elif user_input == 's':
                    self.show_stats()
                else:
                    self.ask_question()
            except KeyboardInterrupt:
                print("\n\n程序已中断。")
                self.show_stats()
                break


if __name__ == "__main__":
    quiz = ArithmeticQuiz()
    quiz.run()