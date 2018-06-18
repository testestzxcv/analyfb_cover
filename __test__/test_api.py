from analyfb_cover.collect.api import api
#
# url = api.fb_gen_url(node='jtbcnews', a=10, b=20, s='kickscar')
#
# print(url)

# id = api.fb_gen_url('jtbcnews')
# print(id)

# url = api.fb_gen_url(
#     node='jtbcnews/posts',
#     fields='id,message',
#     since='2016-01-01',
#     until='2017-04-31',
#     limit=50,
#     access_token='EAACEdEose0cBAKdCAnaaNsA7b9indVorNmsTynvzM04yfZCIit9bvcKvmZCRJD4Q9cKzCNzAcUjNZANXDMhda9ibJXu1O97ybNctpnzn5ZCZA3PLho8vgDOakTAMICmEtw4LfTAytVfTTyOKN2mvQuZBkr94q3ElZB1csaW6JM0XdZAKIJSaXW9OkrAfotsv2sdZBT5bjxTnVqfvrSHOvpnog7jxyLCXx6s0ZD'
#
# )
#
# print(url)

# url = api.fb_name_to_id('jtbcnews')
#
# print(url)

for posts in api.fb_fetch_posts('jtbcnews','2017-01-01','2017-12-31'):
    print("posts:",posts)