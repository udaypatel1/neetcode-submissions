class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []

        for roid in asteroids:

            while st and st[-1] > 0 and roid < 0:

                # same size → both explode
                if st[-1] == -roid:
                    st.pop()
                    break

                # stack asteroid larger → current explodes
                elif st[-1] > -roid:
                    break

                # current larger → destroy stack asteroid
                else:
                    st.pop()

            else:
                st.append(roid)

        return st