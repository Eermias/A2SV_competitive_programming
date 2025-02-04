class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        for domain in cpdomains:
            freq, dom = domain.split()
            dom = dom.split('.')

            if len(dom) == 3:
                dom1 = dom[0] + '.' + dom[1] + '.' + dom[2]
                dom2 = dom[1] + '.' + dom[2]
                
                count[dom1] += int(freq)
                count[dom2] += int(freq)
                count[dom[2]] += int(freq)
            else:
                dom1 = dom[0] + '.' + dom[1]
                dom2 = dom[1]
                
                count[dom1] += int(freq)
                count[dom2] += int(freq)

        return [f"{count[dom]} {dom}" for dom in count]
            