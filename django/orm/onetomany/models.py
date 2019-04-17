from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    
#User:Post = 1:N

class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#User:Comment = 1:N
#Post:Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    
#ex) 1. 1번 user가 작성한 게시글은?
#user1.post_set.all()

#ex) 2. 1번 사람이 작성한 게시글의 댓글들을 출력
#for post in user1.post_set.all():
#   for comment in post.comment_set.all():
#       print(comment.content)

#ex)3. 2번 댓글을 쓴 사람은
#c2.user

#ex)4. 2번 댓글을 쓴 사람이 작성한 게시글을 조회
#c2.user.post_set.all()

#ex)5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
#post1.comment_set.first().user.name

#ex)6. '1글'이 제목인 게시글은?
#Post.objects.filter(title='1글')

#ex)7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
#Comment.objects.filter(post__title='1글') 혹은
#post1 = Post.objects.get(title='1글')
#Comment.objects.filter(post=post1)

#ex)8. 댓글 중에 해당 게시글의 제목에 1이 들어가 있는 것은?


#user1.comment_set.all()
    
# user1 = User.objects.create(name = 'Kim')
# user2 = User.objects.create(name = 'Lee')

# post1 = Post.objects.create(title = '1글', user_id = user1.id) #user = user1 과 같은 의미
# post2 = Post.objects.create(title = '2글', user = user1)
# post3 = Post.objects.create(title = '3글', user = user2)

# c1 = Comment.objects.create(content = '1글 댓글 1', user = user1, post = post1)
# c2 = Comment.objects.create(content = '1글 댓글 2', user = user2, post = post1)
# c3 = Comment.objects.create(content = '1글 댓글 3', user = user1, post = post1)
# c4 = Comment.objects.create(content = '1글 댓글 4', user = user2, post = post1)
# c5 = Comment.objects.create(content = '2글 댓글 1', user = user1, post = post2)
# c6 = Comment.objects.create(content = '!1글 댓글 5', user = user2, post = post1)
# c7 = Comment.objects.create(content = '!2글 댓글 2', user = user2, post = post2)