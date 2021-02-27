import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import json

plt.rcParams['font.family'] = ['Times New Roman']

fontsize = 14
plt.rcParams['font.size'] = fontsize


plt.figure(figsize=(6, 4))

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.25)
# fig = plt.figure()
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#绘制并列柱状图
bar_width = 0.4

x = 2 * np.arange(10)

aff = [0.13, 0.21, 0.27, 0.13, 0.23, 0.15, 0.24, 0.3, 0.35, 0.37]
tick_label10000 = ["BERT\n + \nGoogleNet", "BERT\n + \nSqueezeNet", "ResNet-50\n + \nBERT", "AlexNet\n + \nSqueezeNet", "ResNet-50\n + \nGoogleNet", "GoogleNet\n + \nSqueezeNet", "BERT\n + \nAlexNet",  "GoogleNet\n + \nAlexNet", "ResNet-50\n + \nSqueezeNet", "ResNet-50\n + \nAlexNet"]
y1_10000 = [67.5121546316392, 27.72844112102773, 66.8136719985465, 64.33272025610101, 57.27446895456253, 39.164575741041716, 22.084149566158025, 10.12940089534967, 35.26697039639559, 2.6332453012973023]
y2_10000 = [67.72413932988722, 30.014083726965975, 68.33091995835828, 64.51004175794498, 58.15842680933311, 42.169183859493316, 18.58142763130518, 16.457837010434936, 38.243263524706066, 7.475369248975978]
y3_10000 = [68.2990102876307, 32.730045919691756, 76.013692366909467, 73.724076672306737, 67.07164441645269, 50.677394304308788, 23.05846850267839, 21.080795503887673, 47.86470815390274, 30.59873069350377]

y3_10001 = [9.137990102876307, 6.730045919691756, 24.013692366909467, 28.724076672306737, 28.07164441645269, 25.677394304308788, 15.05846850267839, 14.580795503887673, 47.86470815390274, 30.59873069350377]

count_10000 = [38, 11, 169, 39, 103, 24, 9, 19, 21, 15]
waittime_10000 = [6581.895000001416, 2064.247999999672, 7568.0179999945685, 14541.6660000009, 5202.541000005789, 1976.094000000041, 4912.237999999896, 8866.816999999806, 1413.719000000041, 3716.6919999998063]





# for i, l in enumerate(tick_label10000):
#     tick_label10000[i] = tick_label10000[i] + "\n" + str(aff[i])

tick_label5000 = ["BERT\n + \nGoogleNet", "BERT\n + \nSqueezeNet", "AlexNet\n + \nSqueezeNet", "ResNet-50\n + \nBERT", "BERT\n + \nAlexNet", "GoogleNet\n + \nSqueezeNet", "ResNet-50\n + \nGoogleNet", "GoogleNet\n + \nAlexNet", "ResNet-50\n + \nSqueezeNet",  "ResNet-50\n + \nAlexNet"]
y1_5000 = [67.5121546316392, 27.72844112102773, 64.33272025610101, 66.8136719985465, 22.084149566158025, 39.164575741041716, 57.27446895456253, 35.26697039639559, 10.12940089534967, 2.6332453012973023]
y2_5000 = [67.72681382008199, 29.77189296358827, 64.79643517974888, 68.33091995835828, 18.58142763130518, 42.534156339378036, 57.84903423097329, 38.323423850488986, 16.440861458368754, 8.17139104627157]
y3_5000 = [8.177621799768557, 4.967963077159595, 20.493260127349128, 24.426329589672243, 8.009030394135959, 19.819492192551188, 28.634179975072943, 39.451838588725025, 20.141383354242688, 31.090502973336623]

tick_label20000 = ["BERT\n + \nGoogleNet", "ResNet-50\n + \nBERT", "BERT\n + \nSqueezeNet", "AlexNet\n + \nSqueezeNet", "GoogleNet\n + \nSqueezeNet", "ResNet-50\n + \nGoogleNet", "BERT\n + \nAlexNet", "ResNet-50\n + \nSqueezeNet", "GoogleNet\n + \nAlexNet", "ResNet-50\n + \nAlexNet"]
y1_20000 = [67.5121546316392, 66.8136719985465, 27.72844112102773, 64.33272025610101, 39.164575741041716, 57.27446895456253, 22.084149566158025, 10.12940089534967, 35.26697039639559, 2.6332453012973023]
y2_20000 = [67.72413932988722, 68.32192369525636, 29.639099802219743, 64.51004175794498, 42.030194359616274, 58.14171833017617, 17.88138752107271, 16.363824563684563, 38.243263524706066, 6.181519702309848]
y3_20000 = [10.756086334576093, 20.418595740533537, 9.611737612457434, 34.62189372123853, 24.955548125113953, 39.10750455697162, 12.626374076494747, 20.780113489867864, 48.42386502785674, 30.59873069350377]

tick_label03 = ["BERT\n + \nSqueezeNet", "BERT\n + \nGoogleNet", "ResNet-50\n + \nBERT", "AlexNet\n + \nSqueezeNet", "ResNet-50\n + \nGoogleNet", "GoogleNet\n + \nSqueezeNet", "ResNet-50\n + \nSqueezeNet", "BERT\n + \nAlexNet", "GoogleNet\n + \nAlexNet", "ResNet-50\n + \nAlexNet"]
y1_03 = [27.72844112102773, 67.5121546316392, 66.8136719985465, 64.33272025610101, 57.27446895456253, 39.164575741041716, 10.12940089534967, 17.584149566158025, 35.26697039639559, 2.6332453012973023]
y2_03 = [29.87282940521305, 67.72413932988722, 67.82547936579905, 39.548106112831235, 57.86316402447551, 33.491172056159805, 16.314051434440003, 9.699778151854805, 38.243263524706066, 7.475369248975978]
y3_03 = [5.121631044496384, 12.60726124509129, 13.9285742097335, 13.283243383988374, 24.685785789466888, 24.254074137042807, 14.580795503887673, 18.55846850267839, 47.86470815390274, 19.32923590814048]

tick_label07 = ["BERT\n + \nGoogleNet", "ResNet-50\n + \nBERT", "BERT\n + \nSqueezeNet", "AlexNet\n + \nSqueezeNet", "ResNet-50\n + \nGoogleNet", "GoogleNet\n + \nSqueezeNet", "BERT\n + \nAlexNet", "ResNet-50\n + \nSqueezeNet", "GoogleNet\n + \nAlexNet", "ResNet-50\n + \nAlexNet"]
y1_07 = [67.5121546316392, 66.8136719985465, 27.72844112102773, 64.33272025610101, 57.27446895456253, 39.164575741041716, 22.084149566158025, 10.12940089534967, 35.26697039639559, 2.6332453012973023]
y2_07 = [67.72413932988722, 68.32192369525636, 30.014083726965975, 64.51004175794498, 58.153254890272734, 42.169183859493316, 22.818419996467203, 16.457837010434936, 38.243263524706066, 7.475369248975978]
y3_07 = [9.063855459319436, 13.32885992198405, 6.730045919691756, 17.475498321111438, 27.147616524129475, 25.677394304308788, 15.05846850267839, 20.580795503887673, 47.86470815390274, 31.65957616811067]


# Threshold Line
# plt.plot([13.4] * 100, np.arange(100), color = "red", linestyle="--")
# Threshold Text
# plt.text(13.5, 95, "Affinity >= ?")


plt.bar(x[-3::],y1_20000[-3::],bar_width,color='#f5c89d',label='Only GPU', edgecolor="black", linewidth=0.6)
plt.bar((x+bar_width)[-3::],y2_20000[-3::],bar_width,color='#aad4a3', label='UCGE+I', edgecolor="black", linewidth=0.6)
plt.bar((x+2 * bar_width)[-3::],y3_20000[-3::],bar_width,color='#fffeae', label='OSAS', edgecolor="black", linewidth=0.6)
plt.xticks((x + 1 * bar_width)[-3::],tick_label20000[-3::])
plt.ylim(0, 60)
plt.xlabel("Task combination", fontweight ='bold')
plt.ylabel("Reduced TCT(%)", fontweight ='bold')

plt.legend(ncol=3, loc='best')
plt.savefig("20000_2.pdf")
plt.show()
