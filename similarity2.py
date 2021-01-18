def SimlarityCalu(Vector1, Vector2):
  Vector1Mod = np.sqrt(Vector1.dot(Vector1))
  Vector2Mod = np.sqrt(Vector2.dot(Vector2))
  if Vector2Mod != 0 and Vector1Mod != 0:
      simlarity = (Vector1.dot(Vector2))/(Vector1Mod*Vector2Mod)
  else:
      simlarity = 0
  return simlarity

  def doc2vec(file_name, model):
    docs = [x.strip().split() for x in codecs.open(file_name, "r", "utf-8".readlines()]
    doc_vec_all = numpy.zeros(docvec_size)
    for d in docs:
          doc_vec_all = doc_vec_all + model.infer_vector(d, alpha=start_alpha, steps=infer_epoch)
    return doc_vec_all