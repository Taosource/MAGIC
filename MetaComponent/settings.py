# ��ģ����һ����������ģ��
# ��ͨ����ʼ��ʱ����Ϣ�Գ�����л�������
# ��������ϵͳ������
# ע��߼�������������ϵͳ�н�������
# �߼����ý���д�뵽����ϵͳ�ж�̬�仯

import json



SETTINGS_FILE = r"../info/settings.json"
SETTINGS_INFO = {}

with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
    SETTINGS_INFO = json.load(f)


print(SETTINGS_INFO)