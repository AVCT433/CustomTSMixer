import tensorflow as tf

def r2_keras(y_true, y_pred):
#   SS_res = K.sum(K.square(y_true - y_pred))
#   SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
#   return 1 - SS_res / (SS_tot + K.epsilon())
  # 잔차 제곱합 (SS_res)
  SS_res = tf.reduce_sum(tf.square(y_true - y_pred))
  # 전체 제곱합 (SS_tot)
  SS_tot = tf.reduce_sum(tf.square(y_true - tf.reduce_mean(y_true)))
  # 결정계수 반환
  return 1 - SS_res / (SS_tot + tf.keras.backend.epsilon())