import os
import grpc

os.environ['CUDA_VISIBLE_DEVICES'] = "0,1"
import mii

name = "deepset/roberta-large-squad2"

generator = mii.mii_query_handle(name + "-qa-deployment")
results = generator.query({
    'question': "What is the greatest?",
    'context': "DeepSpeed is the greatest"
})
print(results.response)