class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        ret = []
        for ele in path.split("/"):
            if ele == "." or ele == "" :
                continue
            elif ele == "..":
                if len(ret) > 0:
                    ret.pop()
            else:
                ret.append(ele)
        
        return "/"+"/".join(ret)

a = Solution()
print a.simplifyPath("/../ptervsMY/../XHZ/PmReT///././om/.///NID/./nb/../////../OzVU/..///////..///.///Fbz/.///JkBLsBPOtaZfJxBsr/////./PlKqDZibpe///BojpVLSKRxwoNTye/DouOLUweLjfjmSVnNB/gkVRoZplAXmDApDcfz/../../TGuyzi/LxiuqfGMIVgSqwjjKn///nrUL/./UXubqdyqDdjYpPjxcK/../skBTmgzFvPvRRUVJZaj/.///./dXMwqDITFGedfD///./../SJsnjqaejDumfKMgfIwa/./AkIkoLqSFqCluW/YFroCAYXGPBhYeIMWl/ie/FMGzVASoRbbFRj/cI/zbVOaYMkHjNj/LO/cHvxnYfEaWabThaWbu/./../lCzgrdFsIcrgTsTNG///qRHYGgDkc/ZNQXkAPmygMEp/./iD/YjpUiwMrRUI///SSeyNJTkkVUNQaEmeO/./YVhKivJXOMBiaF/tnyodagYEHDRZaHXFF/mKZLDarbdM/../FgaTiMQHaULpidm/../Rs/.././mSovxOdRAsqApStB/././QgTXzkoJ/../BR/jyUfTCJx/MkXYqXcXFUo///../EdLxgz/./GNrHjtXIwSvKGKr/./KdPo/QlpxuwxRk///Z/KX/JKPkjMrhZ/./////.././//////zXDkQvxQHRj/kcVCaMpRRTbrpjqJ///zMPHxrk/././H///LxRIytui///QsPZecj/////../WKyepNvAXv/JKSJoymertVFOQZgy/eyChfvJciPRaqc/kQDMydOjqDCUeiMF/../PSWbWSmPbNjRxMePqP///qLGDZwcNVSnWz/HvXN///WSWg/esoKtXeevuWTrQFEBlX/./zisxX/../EsUvBkbmtXZgRPeBdqA/DFGWEcQUtgsGlMyB/RduYIuxsCHyCnaDywQRq/TDZCpShqrw/.///tmiRNSCoygMYBcY/fKdCfOzMLZnjOcaOJula/.././wW/./JBMLkAuH/Wxi/uVovvcTKWRviPqjhnm/uJk/../glZFVEVPG/SdwxUNmDirhnl/AqJfZ///../sgWRJUqyJG/./nKtZIW/DhopPsvKicLISLoJjYZ/JBnNVrEzRA/./XK/.///KyKqy/.././//kkdrwuvBdXJPBQW/ULhGXIghUqXk")