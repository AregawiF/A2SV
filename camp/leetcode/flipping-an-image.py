class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for im in image:
            left = 0
            right = len(im) -1
            while left < right:
                im[left], im[right] = im[right], im[left]
                left += 1
                right -= 1
        for im in image:
            for i in range(len(im)):
                if im[i] == 0:
                    im[i] = 1
                else:
                    im[i] = 0
        return image
