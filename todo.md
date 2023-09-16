
-api
-postman
-users
-orders
-cart 
-coupons
-docker
-ccelery
-translation 
-cashing
-redis
-deploy
-ajax



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- def new_post(request,post_id):
-     if request.method == 'POST':
-         form = PostForm(request.post,request.FILES)
-         if form.is_valid():
-             myform= form.save(commit=false)
-             myform.author = request.user
-             myform.save()
-             return redirect('/blog')
-         else:
-             form = PostForm()
-         return render(request,'new_post.html',{'form':form})  
-     return myform.save()

                                                                                                       




    
      


- def edit_post(request,post_id):
-     data = Post.Objects.get(id=post_id)
-     if request.method == 'POST':
-         form = PostForm(request.post,request.FILES,instance=data)
-         if form.is_valid():
-             myform= form.save(commit=false)
-             myform.author = request.user
-             myform.save()
-             return redirect('/blog')
-         else:
-             form = PostForm(instance=data)
-         return render(request,'new_post.html',{'form':form})  
-     return myform.save()
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------