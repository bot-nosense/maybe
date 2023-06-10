
NATURE_TYPE = {
    'xuôi': 'Yes.',
    'ngược': 'No.',
}

ONLY_MINOR_ARCANA_TYPE = {
    'Wands': 'Yes.',
    'Cups': 'No.',
    'Chalices': 'No.',
    'Pentacles': 'No.',
    'Swords': 'Yes.',
}

MEANING_TYPE = {
    'Wands': 'Yes, nhưng bạn phải nỗ lực để có được điều đó.',
    'Cups': 'Yes, chắc chắn bạn sẽ có được điều bạn muốn mà không càn phải làm gì cả.',
    'Chalices': 'Yes, chắc chắn bạn sẽ có được điều bạn muốn mà không càn phải làm gì cả.',
    'Pentacles': 'Yes, bạn sẽ phải có một sự đánh đổi, trả giá để có được nó.',
    'Swords': 'No.',
}

SERVER_NAME = 'DESKTOP-OTE2BAT'
DATABASE_NAME = 'TAROT_DOT_VN'
DRIVER_NAME = '{SQL Server}'
CONNECT_SSMS_STRING = 'Driver=' + DRIVER_NAME + ';Server=' + SERVER_NAME + ';Database= '+ DATABASE_NAME +';Trusted_Connection=yes;'


# gồm ý nghĩa tích cực và tiêu cực
MEANING_OF_THE_CARD = {

    'The Fool - xuôi': {

        'sự khởi đầu', 
        'tích cực, lạc quan,sự vui vẻ, tươi mới', 
        'sự háo hức, tò mò với câu chuyện phía trước', 
        'trải nghiệm mới', 
        'không quan tâm tới phía trước',
        'không sọ hãi, không chùn bước',
        'dũng cảm',
        'năng động, nhiệt huyết',
        'dám nghĩ dám làm',
        'ra khỏi vùng an toàn',
        'làm 1 thứ gì đo mới mẻ, khác đi với những thường ngày',
        'sắp tới công việc mới, 1 công việc chưa làm bao giờ',
        'phải cẩn trọng, đi từng bước 1',

        'sự ngây thơ, bất cần',
        'không có kế hoạch, chiến lược rõ ràng',
        'năng lượng khá trẻ, sự trẻ trung này maybe, nó có cả tiêu cực lẫn tích cực',
        'thiếu cẩn trọng, cẩn thận',
        'thích thử cái mới mà không quan tâm tới kết quả, bất cần',
        'bốc đồng',
        'không nghĩ được xa, không lường trước được kết quả',
        'dễ thất bại',
    },

    'The Fool - ngược': {

    },

    'The Magician - xuôi': {
        'nhận biết được bản thân như thế nào',
        'địa diện cho năng lượng nam tính',
        'chủ động, giỏi giang',
        'biết nắm bắt cơ hội, nhận biết được lúc nào đang làm gì, lúc nào không nên làm gì',

        'hơi kiêu ngạo, luôn trong tâm thế hành động',
        'cần chậm lại 1 chút để suy xét',
        'cho rằng hành động đó là đúng',
        'thiếu sự bình tĩnh',
        
    },

    'The Magician - ngược': {},

    'The High Priestess - xuôi': {
        '',
    },
    'The High Priestess - ngược': {},
    'The Empress - ngược': {},
    'The Empress - xuôi': {},
}

