import tensorflow as tf
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow_note.pool import LeNet5
from tensorflow_note.pool import Baseline
from tensorflow_note.pool import MnistModel
from tensorflow_note.pool import AlexNet8
from tensorflow_note.pool import VGGNet

test=True
save_weights=True
train=False
save_txt=False

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train=np.reshape(x_train,[60000,28,28,1])
x_test=np.reshape(x_test,[10000,28,28,1])
x_train,x_test=x_train/255.,x_test/255.

#model=MnistModel()#全连接网络
#model=LeNet5()#LeNet5网络
#model=Baseline()#基本卷积神经网络模型
#model=AlexNet8()#AlexNet8网络
model=VGGNet()

model.compile(optimizer='adam',
             loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
             metrics=['sparse_categorical_accuracy'])

if save_weights==True:
    checkpoint_save_path='./checkpoint/'+model.net_name+'/mnist.ckpt'
    if os.path.exists(checkpoint_save_path+'.index'):
        print('------------load the model----------')
        model.load_weights(checkpoint_save_path)
        
    cp_callback=tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                save_weights_only=True,#只保留权重
                                                save_best_only=True)#只保留最优
    if train==True:
        history=model.fit(x_train,y_train,batch_size=32,epochs=5,validation_data=(x_test,y_test),validation_freq=1,
                        callbacks=[cp_callback])#预测结果时不用训练
    if save_txt==True:
        file=open('./weights/'+model.net_name+'/weight.txt','w')
        for v in model.trainable_variables:
            file.write(str(v.name)+'\n')
            file.write(str(v.shape)+'\n')
            file.write(str(v.numpy())+'\n')
        file.close()
else:
    if train==True:
        history=model.fit(x_train,y_train,batch_size=32,epochs=5,validation_data=(x_test,y_test),validation_freq=1)

if train==True:
    model.summary()

    acc=history.history['sparse_categorical_accuracy']
    val_acc=history.history['val_sparse_categorical_accuracy']
    loss=history.history['loss']
    val_loss=history.history['val_loss']

    plt.subplot(1,2,1)
    plt.plot(acc,label='Training Accuracy')
    plt.title('Validation and Training Accuracy')
    plt.plot(val_acc,label='Validation Accuracy')
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(loss,label='Training Loss')
    plt.title('Validation and Training Loss')
    plt.plot(val_loss,label='Validation Loss')
    plt.legend()
    plt.show()

if test==True:
    preNum=int(input('input the number of test pictures:'))
    for i in range(preNum):
        image_path=input('the path of test pictures')
        img=Image.open(image_path)
        img=img.resize((28,28),Image.ANTIALIAS)
        img_arr=np.array(img.convert('L'))
        
        #mnist数据集都是黑底白字，需要颜色反转，且增加对比度
        for i in range(28):
            for j in range(28):
                if img_arr[i][j]>160:
                    img_arr[i][j]=0
                else:
                    img_arr[i][j]=255
        #img_arr=255-img_arr#两种方法选其一就行
        plt.imshow(img_arr,cmap='gray')
        plt.show()
        img_arr=img_arr/255.
        x_predict=img_arr[tf.newaxis,...,tf.newaxis]#w喂入神经网络前都是按照batch送入，因此变成[1,28,28]大小的图片
        result=model.predict(x_predict)
        pred=tf.argmax(result,axis=1)
        print('\n')
        tf.print(pred)