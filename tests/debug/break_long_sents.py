# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-04-03 20:33
from hanlp.utils.string_util import split_long_sent


def main():
    delimiter = set()
    delimiter.update('。！？：；、，,;!?、,')
    print([x for x in split_long_sent(
        ['中', '方', '愿', '与', '东', '盟', '国', '家', '在', '业', '已', '建', '立', '的', '基', '础', '上', ',', '培', '育', '新', '的',
         '合', '作', '点', ',', '增', '强', '优', '势', '互', '补', ',', '即', '在', '深', '化', '经', '贸', '合', '作', '的', '同', '时',
         ',', '将', '合', '作', '领', '域', '拓', '展', '至', '资', '源', '开', '发', ',', '农', '业', ',', '适', '用', '技', '术', ',',
         '医', '药', '卫', '生', ',', '人', '力', '资', '源', '开', '发', ',', '环', '保', '等', '领', '域', ',', '尤', '其', '是', '增',
         '加', '科', '技', '合', '作', '的', '比', '重', ',', '加', '强', '金', '融', ',', '商', '务', '信', '息', '的', '交', '流', ',',
         '以', '促', '进', '各', '自', '结', '构', '调', '整', '和', '增', '长', '方', '式', '的', '转', '变', '。'],
        delimiter, 126)])


if __name__ == '__main__':
    main()
