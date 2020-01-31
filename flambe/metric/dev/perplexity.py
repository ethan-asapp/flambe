from typing import Optional
import torch

from flambe.metric import Metric


class Perplexity(Metric):
    """Token level perplexity, computed a exp(cross_entropy)."""

    def __init__(self, name: Optional[str] = None):
        """
        Perplexity, computed as CrossEntropy
        Parameters
        ----------
        name: Optional[str]
            a name for this metric object
        """
        super().__init__(name)
        self.entropy = torch.nn.CrossEntropyLoss()

    def compute(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Compute the preplexity given the input and target.

        Parameters
        ----------
        pred: torch.Tensor
            input logits of shape (B x N)
        target: torch.LontTensor
            target tensor of shape (B)

        Returns
        -------
        torch.float
            Output perplexity

        """
        entropy = self.entropy(pred, target).mean()
        return torch.exp(entropy)
