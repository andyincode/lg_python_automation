# -*- encoding: cp949 -*-

# ���ڶ� ������ ������ ���������� �Ľ̰���
text = '1109200102516918221elias.kim'
print 'Len:', len(text)
zip_code = text[:6]
cell_phone = text[6:17]
age = text[17:19]
name = text[19:]

print 'Zip Code:', zip_code
print 'Cell Phone:', cell_phone
print 'Age:', age
print 'Name:', name
print '#' * 100

# ����, �ѱ�, ������ ���������� ������ �������� �Ľ̺Ұ�
text = '110920���ϰ��̿�������������21elias.kim'
print 'Len:', len(text)
zip_code = text[:6]
cell_phone = text[6:17]
age = text[17:19]
name = text[19:]

print 'Zip Code:', zip_code
print 'Cell Phone:', cell_phone
print 'Age:', age
print 'Name:', name
print '#' * 100

# �����ڵ�� ��ȯ�� ������ �������� �Ľ̰���
text = '110920���ϰ��̿�������������21elias.kim'
print 'Len:', len(text)
# uni_text = text.decode()  # Error
# uni_text = text.decode('utf-8') # Error
# uni_text = text.decode('utf8') # Error
uni_text = text.decode('cp949')
print 'Len:', len(uni_text)
zip_code = uni_text[:6]
cell_phone = uni_text[6:17]
age = uni_text[17:19]
name = uni_text[19:]
print '#' * 100

print 'Zip Code:', zip_code
print 'Cell Phone:', cell_phone
print 'Age:', age
print 'Name:', name
print '#' * 100

import sys
print(sys.stdin.encoding)