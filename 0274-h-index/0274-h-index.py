class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers_count = len(citations)
        citation_frequency = [0]*(papers_count + 1)

        for citation in citations:
            citation_frequency[min(citation, papers_count)] += 1

        papers_sum = 0
        for h_index in range(papers_count, -1, -1):
            papers_sum += citation_frequency[h_index]
            if papers_sum >= h_index:
                return h_index    
