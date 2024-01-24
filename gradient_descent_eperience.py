import math
import random
import time
import xlwt


# 辅助投篮机函数完成概率和结果计算
def probability(pro):
    choices = [1, 0]  # 1 表示命中，0 表示未命中
    weights = [pro, 1 - pro]  # 设置权重，以达到所需的命中概率
    result = random.choices(choices, weights=weights, k=1)
    return result[0]


# 定义投篮机函数，接受三个参数，返回命中结果和距离
def basketball(ss, ha, pa):
    d = math.sqrt((ss - 100) * (ss - 100) + ha * ha / 0.04 + (pa - 45) * (pa - 45) / 0.04)  # 计算离画面中心的距离
    # d = math.sqrt((ss+random.random() - 100) *(ss+random.random() - 100) + (ha+ 0.05 * random.randint(-1, 1)) *(ha+ 0.05 * random.randint(-1, 1)) / 0.04 + (pa - 45+0.05*random.randint(-1,1)) * (pa - 45+0.05*random.randint(-1,1))/ 0.25)  # 计算离画面中心的距离
    if d >= 1:  # 计算命中率
        pw = 0
    elif 0 <= d < 1:
        pw = -(d * d) + 1
    ppw = pw * 100  # 命中概率
    bingo = probability(ppw)  # 调用函数并获取命中结果
    return bingo, d  # 返回命中结果和离中心距离d


experience_prob = {}  # 建立该程序的经验字典。后面的需要记忆的放入其中。
exp_num = 1000  # 每个位置用几次测量求命中概率。


def baoliu3wei(ss, ha, pa):
    ss = round(ss, 3)
    ha = round(ha, 3)
    pa = round(pa, 3)


def panduanjingyan(ss, ha, pa):
    if not ((ss, ha, pa) in experience_prob):
        experience_prob[(ss, ha, pa)] = 0
        return 0  # 之前没有过这组组合
    else:
        # print((ss, ha, pa) in experience_prob)
        return 1  # 之前已经有过了这组组合


def experience_record(ss, ha, pa, exp_num):
    baoliu3wei(ss, ha, pa)
    if panduanjingyan(ss, ha, pa) == 0:
        for i in range(exp_num):
            ss_random = 2 * random.random() - 1
            ha_random = 0.05 * random.randint(-1, 1)
            pa_random = 0.05 * random.randint(-1, 1)
            # ss_random = 0
            # ha_random = 0
            # pa_random = 0
            ss_current = ss + ss_random  # 本轮的SS
            ha_current = ha + ha_random  # 本轮的HA
            pa_current = pa + pa_random  # 本轮的PA
            result = basketball(ss_current, ha_current, pa_current)  # 计算本次的投篮结果。
            experience_prob[(ss, ha, pa)] = (i * experience_prob[(ss, ha, pa)] + result[0]) / (i + 1)
            # print(f"the probability of ss：{ss},ha:{ha},pa:{pa}={experience_prob[(ss, ha, pa)]},i={i}")
        print("第一次出现位置")
        print(f"the probability of ss：{ss},ha:{ha},pa:{pa}={experience_prob[(ss, ha, pa)]},i={i}")
    else:
        print("多次出现位置")
    return

    # 定义均方误差损失函数


def mse_loss(predicted_distance, target_distance):
    return (predicted_distance - target_distance) ** 2


# 初始参数，随机值
ss = 98
ha = -1
pa = 44

# 目标距离
target_distance = 0.0  # 目标是命中

# 学习率
learning_rate = 0.01

# 开始训练
iterations = 1  # 计数器
time_start = time.time()  # 计时开始

# 创建一个新的 Excel 文件和工作表
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Parameters')

# 添加 Excel 表头
sheet.write(0, 0, 'Iteration')
sheet.write(0, 1, 'Parameter 1 (ss)')
sheet.write(0, 2, 'Parameter 2 (ha)')
sheet.write(0, 3, 'Parameter 3 (pa)')
sheet.write(0, 4, 'Output Parameter (d)')
sheet.write(0, 5, 'Output hit probability')

sheet.col(1).width = 256 * (len('Parameter 1 (ss)') + 2)
sheet.col(2).width = 256 * (len('Parameter 2 (ha)') + 2)
sheet.col(3).width = 256 * (len('Parameter 3 (pa)') + 2)
sheet.col(4).width = 256 * (len('Output Parameter (d)') + 2)
sheet.col(5).width = 256 * (len('Output hit probability') + 2)
row_index = 1  # 创建 Excel 表的行索引

# 设置样式，禁止科学计数法
style = xlwt.easyxf(num_format_str='0.00000000')

episode = 500  # 循环次数
for iteration in range(episode):
    # 计算当前参数下的距离
    ss_random = 2 * random.random() - 1
    ha_random = 0.05 * random.randint(-1, 1)
    pa_random = 0.05 * random.randint(-1, 1)
    # ss_random = 0
    # ha_random = 0
    # pa_random = 0
    ss_current = ss + ss_random  # 本轮的SS
    ha_current = ha + ha_random  # 本轮的HA
    pa_current = pa + pa_random  # 本轮的PA
    dis = basketball(ss_current, ha_current, pa_current)
    print("当前的随机误差", "ss:", ss_random, "ha:", ha_random, "pa:", ha_random)
    # dis = basketball(ss , ha , pa)
    distance = dis[1]

    # 训练提示
    print("正在进行第:", iteration + 1, "轮训练")
    print("当前参数: ss:", ss, "ha:", ha, "pa:", pa, "距离D:", distance)

    experience_record(ss, ha, pa, exp_num)
    sheet.write(row_index, 0, iteration + 1)
    sheet.write(row_index, 1, ss, style)
    sheet.write(row_index, 2, ha, style)
    sheet.write(row_index, 3, pa, style)
    sheet.write(row_index, 4, dis[1], style)
    baoliu3wei(ss, ha, pa)
    sheet.write(row_index, 5, experience_prob[(ss, ha, pa)], style)
    row_index += 1

    # 计算损失函数
    loss = mse_loss(distance, target_distance)

    # if loss < 0.0001:  # 使用损失来判断是否结束训练,即d<0.01时
    #   break

    # 数值近似计算参数的梯度
    epsilon = 0.1  # 微小的变化量
    gradient_ss = (mse_loss(basketball(ss_current + epsilon, ha_current, pa_current)[1],
                            target_distance) - mse_loss(
        basketball(ss_current - epsilon, ha_current, pa_current)[1], target_distance)) / (
                          2 * epsilon)  # 估计函数在ss上的变化率，作为梯度的近似值
    gradient_ha = (mse_loss(basketball(ss_current, ha_current + epsilon, pa_current)[1],
                            target_distance) - mse_loss(
        basketball(ss_current, ha_current - epsilon, pa_current)[1], target_distance)) / (
                          2 * epsilon)  # 估计函数在ha上的变化率，作为梯度的近似值
    gradient_pa = (mse_loss(basketball(ss_current, ha_current, pa_current + epsilon)[1],
                            target_distance) - mse_loss(
        basketball(ss_current, ha_current, pa_current - epsilon)[1], target_distance)) / (
                          2 * epsilon)  # 估计函数在pa上的变化率，作为梯度的近似值

    # 使用梯度下降更新参数
    ss -= learning_rate * gradient_ss
    ha -= learning_rate * gradient_ha
    pa -= learning_rate * gradient_pa

# 计时结束
time_end = time.time()
all_time = time_end - time_start  # 总时间

# 输出结果保留3位小数
formatted_ss = format(ss, '.3f')
formatted_ha = format(ha, '.3f')
formatted_pa = format(pa, '.3f')
formatted_distance = format(distance, '.3f')
# baoliu3wei(ss, ha, pa)
# formatted_experience = format(experience_prob[(ss, ha, pa)], '.3f')


workbook.save('gradient_descent.xls')

print("训练完成！")
print("最佳参数：ss =", formatted_ss, "ha =", formatted_ha, "pa =", formatted_pa)
print("最终距离：", formatted_distance)
print("训练轮数：", iterations, "轮")
print("训练用时:", all_time, "s")
