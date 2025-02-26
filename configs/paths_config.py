dataset_paths = {
	'celeba_train': '',
	'celeba_test': '',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '',

	'zookiz_sketch_train': './new_sketch_train',
  	'zookiz_train': './new_target_train', 
  	'zookiz_test_sktech': './new_sketch_test',
  	'zookiz_test':'./new_target_test'
}

model_paths = {
   'stylegan_ffhq' : './pretrained_models/network-snapshot-003894.pt',
	'ir_se50': './pretrained_models/model_ir_se50.pth',
	'circular_face': './pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': './pretrained_models/pnet.npy',
	'mtcnn_rnet': './pretrained_models/rnet.npy',
	'mtcnn_onet': './pretrained_models/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	# 'moco': '/content/drive/MyDrive/stylegan_exp01/try02/pretrained_models/moco_v2_800ep_pretrain.pt'
}
